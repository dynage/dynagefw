from dynagefw.fw_utils import delete_lhab_info
import argparse

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='checks jobs in analysis')
#
#     parser.add_argument('analysis_id_file', help='pickle file')
#     parser.add_argument('--api-key', dest='api_key', action='store', required=False,
#                         help='API key. If not passed, looks for env var "FWAPI"')
#     args = parser.parse_args()

delete_lhab_info("lhab_mini","lhab")
