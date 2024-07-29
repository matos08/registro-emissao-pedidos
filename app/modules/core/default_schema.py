from fastapi_camelcase import CamelModel


class DefaultSchema(CamelModel):
    """
    Schema for return a message.
    """

    detail: str
