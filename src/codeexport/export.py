import json
from my.coding.commits import commits
from my.config import commits as user_config

class Exporter:
  def commit_to_dict(c) -> dict:
      """
      Convert a Commit object to a dictionary format.
      """
      return {
          "committed_dt": c.committed_dt.isoformat(),
          "authored_dt": c.authored_dt.isoformat(),
          "message": c.message,
          "repo": c.repo,
          "sha": c.sha,
          "ref": c.ref
      }

  def export_json():
      """
      Exports the commits to a JSON file specified by the export_path in the config.
      """
      commit_list = [commit_to_dict(c) for c in commits()]

      export_path = config().export_path
      if not export_path:
          raise ValueError("Export path is not set in the user configuration.")

      export_file = str(export_path[0])  # assuming export_path is a list with a single entry

      with open(export_file, 'w', encoding='utf-8') as f:
          json.dump(commit_list, f, ensure_ascii=False, indent=4)

      print(f"Commits exported to {export_file}")

def main() -> None:
    parser = make_parser()
    args = parser.parse_args()

    params = args.params
    dumper = args.dumper

    j = get_json(**params)
    js = json.dumps(j, ensure_ascii=False, indent=1)
    dumper(js)


def make_parser():
    from .exporthelpers.export_helper import setup_parser, Parser
    parser = Parser(''''''.strip())
    # TODO repositories?
    setup_parser(
        parser=parser,
        params=[],
        extra_usage='''
You can also import ~codeexport.export~ as a module and call ~get_json~ function directly to get raw JSON.
        ''',
    )
    return parser



if __name__ == '__main__':
    main()
