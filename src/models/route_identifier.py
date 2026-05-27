"""
Route identifier model.
"""

from typing import Literal

from pydantic import BaseModel, Field


class RouteIdentifier(BaseModel):
    """Model for routing queries to appropriate nodes."""

    route: Literal["index", "general", "search"] = Field(
        description=(
            "The routing decision. Must be exactly one of: "
            "'index' if the provided context is relevant and sufficient to answer the question; "
            "'general' if the context is not relevant but the question can be answered from common knowledge; "
            "'search' if the answer requires external, real-time, or niche information."
        )
    )
