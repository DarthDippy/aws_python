import boto3


def get_profile_role(_account):
    # example of having multiple accounts. Probably should be in its own configuration instead of code
    _account_roles = {
        "some_acccount_1": {
            "profile_name": "Some_Profile_Name1",
            "arn_role": "arn:aws:iam::1234:role/somerolename"
        },
        "some_acccount_2": {
            "profile_name": "Some_Profile_Name2",
            "arn_role": "arn:aws:iam::12345:role/somerolename"
        }
    }

    return _account_roles[_account]


def get_session(_environment, profile_role):
    if _environment == "local":
        return boto3.Session(profile_name=profile_role["profile_name"])

    sts = boto3.client('sts')

    response = sts.assume_role(
        RoleArn=profile_role["arn_role"],
        RoleSessionName='MySession'
    )

    credentials = response["Credentials"]

    return boto3.Session(
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials["SessionToken"]
    )