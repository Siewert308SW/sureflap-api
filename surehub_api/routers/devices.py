from typing import List, Annotated, Any

from fastapi import APIRouter, Query

from surehub_api.entities import official
from surehub_api.entities.openapi import Tags
from surehub_api.services import devices

router = APIRouter(
    prefix="/devices",
    tags=[Tags.DEVICE],
)


@router.get("/",
            response_model_exclude_none=True)
async def get_devices(
        household_ids: Annotated[List[int], Query()] = None
) -> List[official.Device]:
    return devices.get_devices(
        household_ids=household_ids
    )


@router.get("/{device_id}",
            response_model_exclude_none=True)
async def get_device_by_id(device_id: int) -> official.Device:
    return devices.get_device_by_id(device_id)


@router.get("/{device_id}/state",
            response_model_exclude_none=True)
async def get_device_state_by_id(device_id: int) -> Any:
    return devices.get_device_state_by_id(device_id)


@router.patch("/{device_id}/state",
              response_model_exclude_none=True)
async def update_device_state(device_id: int, device_state: official.DeviceControl) -> official.DeviceControl:
    return devices.update_device_state(device_id, device_state)


@router.get("/{device_id}/tags",
            response_model_exclude_none=True)
async def get_tags_of_device(device_id: int) -> List[official.DeviceTag]:
    return devices.get_tags_of_device(device_id)


@router.get("/{device_id}/tags/{tag_id}",
            response_model_exclude_none=True)
async def get_tag_of_device(device_id: int, tag_id: int) -> official.DeviceTag:
    return devices.get_tag_of_device(device_id, tag_id)


@router.put("/{device_id}/tags/{tag_id}",
            response_model_exclude_none=True)
async def assign_tag_to_device(device_id: int, tag_id: int) -> official.DeviceTag:
    return devices.assign_tag_to_device(device_id, tag_id)


@router.delete('/{device_id}/tags/{tag_id}',
               response_model_exclude_none=True)
def remove_tag_from_device(device_id: int, tag_id: int) -> official.DeviceTag:
    return devices.remove_tag_from_device(device_id, tag_id)
