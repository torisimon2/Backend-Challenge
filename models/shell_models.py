from sqlmodel import Field, SQLModel

class ShellBase(SQLModel):
    name: str = Field(title="Name of the shell")
    species: str = Field(title="Species the shell belongs to")
    description: str | None = Field(default=None, title="Physical description of the shell")
    size_cm: float | None = Field(default=None, title="Size in centimeters of the shell")
    location_found: str | None = Field(default=None, title="The location where the shell was found")

class Shell(ShellBase, table=True):
    id: int | None = Field(default=None, primary_key=True, nullable=False)

class ShellPublic(ShellBase):
    id: int

class ShellCreate(ShellBase):
    pass

class ShellUpdate(ShellBase):
    name: str | None = None
    species: str | None = None
    description: str | None = None
    size_cm: float | None = None
    location_found: str | None = None
