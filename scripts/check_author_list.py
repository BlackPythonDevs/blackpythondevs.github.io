import frontmatter
import glob
import os
import sys

POSTS_DIR = "_posts"


def check_authors():
    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    failed = False
    for file_path in files:
        try:
            post = frontmatter.load(file_path)
            if "author" in post.metadata:
                author = post.metadata["author"]
                if not isinstance(author, list):
                    print(f"Error: Author in {file_path} is not a list: {author}")
                    failed = True
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            failed = True

    if failed:
        sys.exit(1)
    else:
        print("All authors are lists.")


if __name__ == "__main__":
    check_authors()
