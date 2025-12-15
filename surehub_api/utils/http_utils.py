from typing import Any

from fastapi import HTTPException

STATUS_CODE_ON_INVALID_RESPONSE = 500


def extract_response_data(
        response,
        key: str = "data",
        status_code_on_invalid: int = STATUS_CODE_ON_INVALID_RESPONSE,
) -> Any:
    """
    Validates an HTTP response and extracts a payload.

    - Raises HTTPException on non-2xx responses
    - Parses JSON safely
    - Validates presence of expected key
    """

    if not response.ok:
        raise HTTPException(
            status_code=response.status_code,
            detail=_extract_error_detail(response),
        )

    try:
        payload = response.json()
    except ValueError:
        raise HTTPException(
            status_code=status_code_on_invalid,
            detail="Response is not valid JSON",
        )

    if key not in payload:
        raise HTTPException(
            status_code=status_code_on_invalid,
            detail=f"Invalid response format: missing '{key}'",
        )

    return payload[key]


def _extract_error_detail(response) -> str | dict:
    try:
        return response.json()
    except ValueError:
        return response.text.replace('"', "'")
