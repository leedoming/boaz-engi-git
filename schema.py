touch schema.py
echo "from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    group: str
" > schema.py
