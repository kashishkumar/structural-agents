from pydantic import BaseModel


class beam_design_input(BaseModel):
    span: float
    load: float
    material: str
    initial_section: str

class beam_design_output(BaseModel):
    material: str
    section: str

