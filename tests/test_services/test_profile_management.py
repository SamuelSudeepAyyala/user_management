import uuid
import pytest

dummy_create_data = {
        "nickname": "Invalid-NickName",
        "email": "invalid@email.com",
        "password": "InvalidPassword",
        "role": "INVALID"
    }

dummy_updated_data = {
        "email": "john.doe@example.com",
        "nickname": "john_doe123",
        "first_name": "John",
        "last_name": "Doe",
        "bio": "Experienced software developer specializing in python applications",
        "profile_picture_url": "https://example.com/profiles/john.jpg",
        "linkedin_profile_url": "https://linkedin.com/in/johndoe",
        "github_profile_url": "https://github.com/johndoe",
        "role": "AUTHENTICATED",
        "is_professional": True
        }
#Testing Creates
@pytest.mark.asyncio
async def test_invalid_role_create(async_client, admin_token):
    
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.post("/users/", json=dummy_create_data, headers=headers)
    assert response.status_code == 422
    error_details = response.json().get("detail", [])

#Testing Updates
@pytest.mark.asyncio
async def test_update_user_dont_exist(async_client, admin_token):
    dummy_user_id = uuid.uuid4()
    
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/profile-update", json=dummy_updated_data, headers=headers)
    assert response.status_code == 400
    assert "User not found" in response.json().get("detail", "")

@pytest.mark.asyncio
async def test_update_self_profile_failure(async_client):
    response = await async_client.put("/profile-update", json=dummy_updated_data)
    assert response.status_code == 401
    
#Testing Promotions
@pytest.mark.asyncio
async def test_promote_user(async_client, admin_user, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/promote/{admin_user.id}/", headers=headers)
    assert response.status_code == 200
    assert response.json()["is_professional"] is True

@pytest.mark.asyncio
async def test_promotion_with_admin_token(async_client,admin_user,admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/promote/{admin_user.id}/", headers=headers)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_promotion_with_manager_token(async_client,manager_user,manager_token):
    headers = {"Authorization": f"Bearer {manager_token}"}
    response = await async_client.put(f"/promote/{manager_user.id}/", headers=headers)
    assert response.status_code == 200
    
@pytest.mark.asyncio
async def test_promotion_with_user_token(async_client,verified_user,user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = await async_client.put(f"/promote/{verified_user.id}/", headers=headers)
    assert response.status_code == 403

