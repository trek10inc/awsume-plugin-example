import argparse
import sys

from awsume.awsumepy import hookimpl, safe_print


@hookimpl
def pre_add_arguments(config: dict):
    safe_print('Before adding arguments')


@hookimpl
def add_arguments(parser: argparse.ArgumentParser):
    try:
        parser.add_argument('--test')
    except argparse.ArgumentError:
        pass


@hookimpl
def post_add_arguments(config: dict, arguments: argparse.Namespace, parser: argparse.ArgumentParser):
    if arguments.test:
        safe_print('Custom flag was triggered')


@hookimpl
def pre_collect_aws_profiles(config: dict, arguments: argparse.Namespace, credentials_file: str, config_file: str):
    safe_print('Before collecting aws profiles')


@hookimpl
def collect_aws_profiles(config: dict, arguments: argparse.Namespace, credentials_file: str, config_file: str):
    return {
        'profile1': {
            'aws_access_key_id': 'AKIA...',
            'aws_secret_access_key': 'SECRET',
            'region': 'us-west-2',
        },
        'profile2': {
            'aws_access_key_id': 'AKIA...',
            'aws_secret_access_key': 'SECRET',
            'mfa_serial': 'arn:aws:iam::123123123123:mfa/user',
        },
        'profile3': {
            'role_arn': 'AKIA...',
            'mfa_serial': 'arn:aws:iam::123123123123:mfa/user',
            'source_profile': 'profile2',
        },
    }


@hookimpl
def post_collect_aws_profiles(config: dict, arguments: argparse.Namespace, profiles: dict):
    safe_print('After collecting aws profiles')


@hookimpl
def pre_get_credentials(config: dict, arguments: argparse.Namespace, profiles: dict):
    safe_print('Before getting credentials')


@hookimpl
def get_credentials(config: dict, arguments: argparse.Namespace, profiles: dict):
    # ... handle getting credentials
    return {
        'AccessKeyId': 'AKIA...',
        'SecretAccessKey': 'SECRET',
        'SessionToken': 'LONGSECRET',
        'Region': 'us-east-2',
    }


@hookimpl
def get_credentials_with_saml(config: dict, arguments: argparse.Namespace):
    # ... handle getting credentials
    return {
        'AccessKeyId': 'AKIA...',
        'SecretAccessKey': 'SECRET',
        'SessionToken': 'LONGSECRET',
        'Region': 'us-east-2',
    }


@hookimpl
def get_credentials_with_web_identity(config: dict, arguments: argparse.Namespace):
    # ... handle getting credentials
    return {
        'AccessKeyId': 'AKIA...',
        'SecretAccessKey': 'SECRET',
        'SessionToken': 'LONGSECRET',
        'Region': 'us-east-2',
    }


@hookimpl
def post_get_credentials(config: dict, arguments: argparse.Namespace, profiles: dict, credentials: dict):
    safe_print('After getting credentials')


@hookimpl
def catch_profile_not_found_exception(config: dict, arguments: argparse.Namespace, profiles: dict, error: Exception):
    safe_print('Uh oh, a profile was not found')


@hookimpl
def catch_invalid_profile_exception(config: dict, arguments: argparse.Namespace, profiles: dict, error: Exception):
    safe_print('Uh oh, a profile was invalid')


@hookimpl
def catch_user_authentication_error(config: dict, arguments: argparse.Namespace, profiles: dict, error: Exception):
    safe_print('Uh oh, could not authenticate the user')


@hookimpl
def catch_role_authentication_error(config: dict, arguments: argparse.Namespace, profiles: dict, error: Exception):
    safe_print('Uh oh, could not authenticate the role')


@hookimpl
def get_profile_names(config: dict, arguments: argparse.Namespace):
    return [
        'profile1',
        'profile2',
        'profile3',
    ]
