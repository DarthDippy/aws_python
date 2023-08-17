from lib import get_profile_role, get_session


if __name__ == "__main__":
    profile_role = get_profile_role("some_acccount_1")
    session = get_session("local", profile_role=profile_role)

    glue_client = session.client("glue", region_name="us-east-1")
