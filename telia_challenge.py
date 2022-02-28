from typing import List, Union


class TeliaChallenge:
    @staticmethod
    def reduce_path(arr: List[str]) -> Union[str, list[str]]:
        """
        Removes needless paths (NORTH<->SOUTH and WEST<->>EAST).

        :param arr: List of strings.

        :return: Same list of strings with removed needless paths.
        """
        for index in range(len(arr) - 1, -1, -1):
            if arr[index - 1 : index + 1] in [
                ["NORTH", "SOUTH"],
                ["SOUTH", "NORTH"],
                ["EAST", "WEST"],
                ["WEST", "EAST"],
            ]:
                del arr[index - 1 : index + 1]
        return arr


if __name__ == "__main__":
    path_array_1 = ["NORTH", "SOUTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]
    print(TeliaChallenge.reduce_path(path_array_1))
    path_array_2 = ["NORTH", "EAST", "NORTH", "SOUTH", "WEST", "SOUTH", "WEST", "WEST"]
    print(TeliaChallenge.reduce_path(path_array_2))
    path_array_2 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]
    print(TeliaChallenge.reduce_path(path_array_2))
    path_array_2 = ["NORTH", "WEST", "SOUTH", "EAST"]
    print(TeliaChallenge.reduce_path(path_array_2))
    path_array_2 = []
    print(TeliaChallenge.reduce_path(path_array_2))
