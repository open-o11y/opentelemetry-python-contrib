# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest


# Series of test cases to ensure config validation works as intended
class TestConfig(unittest.TestCase):
    def test_valid_standard_config(self):
        pass

    def test_valid_basic_auth_config(self):
        pass

    def test_valid_bearer_token_config(self):
        pass

    def test_valid_quantiles_config(self):
        pass

    def test_valid_histogram_boundaries_config(self):
        pass

    def test_valid_tls_config(self):
        pass

    def test_invalid_no_url_config(self):
        pass

    def test_invalid_no_name_config(self):
        pass

    def test_invalid_no_remote_timeout_config(self):
        pass

    def test_invalid_no_username_config(self):
        pass

    def test_invalid_no_password_config(self):
        pass

    def test_invalid_conflicting_passwords_config(self):
        pass

    def test_invalid_conflicting_bearer_tokens_config(self):
        pass

    def test_invalid_conflicting_auth_config(self):
        pass

    def test_invalid_quantiles_config(self):
        pass

    def test_invalid_histogram_boundaries_config(self):
        pass

    # Verifies that valid yaml file is parsed correctly
    def test_valid_yaml_file(self):
        pass

    # Ensures invalid filepath raises error when parsing
    def test_invalid_yaml_file(self):
        pass
