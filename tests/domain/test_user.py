def test_user_creation():
    from domain.models.user import User
    user = User(name="Test User")
    assert user.name == "Test User"