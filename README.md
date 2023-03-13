# Pydantic Type Plus

Working in progress

## Usage

```python
from pydantic_type_plus import UInt32, UInt16, UInt8
from pydantic import BaseModel
from typing import Optional


class TestModel(BaseModel):
    uint32: UInt32
    uint16: UInt16
    uint8: UInt8


model = TestModel(uint32=10000000, uint16=10000, uint8=250)

print(model) # uint32=UInt32(10000000) uint16=UInt16(10000) uint8=UInt8(250)
```