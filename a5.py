import os
def count_characters(filename):
 

  with open(filename, "r") as f:
    characters = len(f.read())

  return characters


def count_words(filename):
  """Counts the number of words in a file."""

  with open(filename, "r") as f:
    words = len(f.read().split())

  return words


def count_lines(filename):


  with open(filename, "r") as f:
    lines = len(f.readlines())

  return lines


def main():
  """The main function."""

  filename = input("Enter file name with complete path: ")



  if not os.path.exists(filename):
    with open(filename, "w") as f:
      print("Enter data to store in file: ")
      data = input()
      while data.upper() != "EOF":
        f.write(data + "\n")
        data = input()

 

  characters = count_characters(filename)
  words = count_words(filename)
  lines = count_lines(filename)



  print("The file {} has {} characters, {} words, and {} lines.".format(
      filename, characters, words, lines))


if __name__ == "__main__":
  main()
