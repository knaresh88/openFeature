import logging
from .providers import HarnessClient

logger = logging.getLogger(__name__)

class FeatureFlagService:
    def __init__(self):
        self.harness_client = HarnessClient(api_key='172f1e96-022a-47cc-bb1b-57f136a87f17')

    def fetch_flag_values(self, flag_name, target_identifier, target_name):
        logger.info("fetch_flag_values() -- start")

        try:
            flag_value = self.harness_client.is_feature_enabled(flag_name, target_identifier, target_name, False)
            logger.info(f"Flag '{flag_name}' resolved with value: {flag_value}")
        except Exception as e:
            logger.error(f"Error fetching flag value: {e}")
            flag_value = False

        logger.info("fetch_flag_values() -- end")
        return flag_value
