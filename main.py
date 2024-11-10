import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Example python script generating an output file")
    parser.add_argument('--input')
    parser.add_argument('--output')

    with open(args.output, "w") as f:
      f.write(",".join(["metric","value"])
      f.write(",".join(["num_reads",100])
      f.write(",".join(["num_aligned",98])
