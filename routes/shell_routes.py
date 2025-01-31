from models.shell_models import Shell, ShellPublic, ShellUpdate, ShellCreate
from fastapi import HTTPException, APIRouter, Depends, Query
from database.database import get_session
from typing import Annotated
from sqlmodel import Session, select

SessionDep = Annotated[Session, Depends(get_session)]

shell_router = APIRouter()

@shell_router.get("/")
def read_root():
    """
    Retrieve the root and display a message to check the application is running.
    """
    return {"message": "Hello Shells :)"}

@shell_router.post("/shells/", response_model=ShellPublic)
def create_shell(shell: ShellCreate, session: SessionDep):
    """
    Create a shell. The body must include the following:
     - **name**: String containing the shell's name
     - **species**: String containing the species the shell belongs to

    The body can optionally include the following:
     - **description**: String containing physical description of the shell
     - **size_cm**: Float containing the size of the shell in centimeters
     - **location_found**: String containing the location where the shell was found

    Upon success code 200 will be returned. Upon failure code 400 will be returned.
    """
    db_shell = Shell.model_validate(shell)
    session.add(db_shell)
    session.commit()
    session.refresh(db_shell)
    return db_shell

@shell_router.get("/shells/", response_model=list[ShellPublic])
def read_shells(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
):
    """
    Retrieve all shells.
     - **offset**: Optional integer query value to specify and offset
     - **limit**: Optional integer query value to specify a limit to return

     Upon success the list of shells will be returned.
    """
    shells = session.exec(select(Shell).offset(offset).limit(limit)).all()
    return shells

@shell_router.get("/shells/{shell_id}", response_model=ShellPublic)
def read_shell(shell_id: int, session: SessionDep):
    """
    Retrieve a specific shell based on the shell ID

    Upon success the specified shell will be returned. If the shell cannot be found code 404 will be returned.
    """
    shell = session.get(Shell, shell_id)
    if not shell:
        raise HTTPException(status_code=404, detail="Shell not found")
    return shell

@shell_router.patch("/shells/{shell_id}", response_model=ShellPublic)
def update_shell(shell_id: int, shell: ShellUpdate, session: SessionDep):
    """
    Update the value(s) of a specific shell bassed on shell ID. The following values can be speficied in the body to change their value:
    - **name**: String containing the new name
    - **species**: String containing the new species
    - **description**: String containing the new description
    - **size_cm**: Float value containing the new size
    - **location_found**: String value containing the new locaton

    Upon success code 200 will be returned and the shell values will be updated. If the shell cannot be found, then code 404 will be returned. If the request cannot be processed, code 400 will be returned.
    """
    shell_db = session.get(Shell, shell_id)
    if not shell_db:
        raise HTTPException(status_code=404, detail="Shell not found")
    shell_data = shell.model_dump(exclude_unset=True)
    shell_db.sqlmodel_update(shell_data)
    session.add(shell_db)
    session.commit()
    session.refresh(shell_db)
    return shell_db

@shell_router.delete("/shells/{shell_id}")
def delete_shell(shell_id: int, session: SessionDep):
    """
    Delete a specific shell based on shell ID.

    Upon success code 200 is returned and the shell is deleted. If the shell cannot be found, code 404 is returned.
    """
    shell = session.get(Shell, shell_id)
    if not shell:
        raise HTTPException(status_code=404, detail="Shell not found")
    session.delete(shell)
    session.commit()
    return {"ok": True}
