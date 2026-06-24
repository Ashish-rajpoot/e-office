from pathlib import Path


class FileManager:

    @staticmethod
    def get_draft_file(mobile_number):
        """
        Returns full path of the user's draft file.
        Searches for any extension.
        """

        root_dir = Path(__file__).resolve().parent.parent
        data_dir = root_dir / "data"

        matches = list(
            data_dir.glob(f"{mobile_number}.*")
        )

        if not matches:
            raise FileNotFoundError(
                f"No draft found for mobile number: "
                f"{mobile_number}"
            )

        return str(matches[0])