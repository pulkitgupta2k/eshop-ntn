import csv

def tabulate(csvfile, matrix):
    with open(csvfile, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(matrix)

def driver():
    clean_results = []
    # with open("results_new.csv") as f:
    #     results_new = csv.reader(f, delimiter=',')
    #     for row in results_new:
    #         if row[-2] == 'Single row tapered roller bearings':
    #             clean_results.append(row[:-1])
    #         elif not row[-1] == 'NOT_COMPLETE':
    #             clean_results.append(row)
    #         else:
    #             # print("REMOVED")
    #             pass
    # print("CLEANED")
    # with open("results_groove.csv") as f:
    #     results = csv.reader(f, delimiter=',')
    #     for row in results:
    #         clean_results.append(row)
    # print("Groove done")
    with open("results_bearing.csv") as f:
        results = csv.reader(f, delimiter=',')
        for row in results:
            clean_results.append(row)
    print("Bearing done")
    tabulate("final_results_2.csv", clean_results)


if __name__ == "__main__":
    driver()