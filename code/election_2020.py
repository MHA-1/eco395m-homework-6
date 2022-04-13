import csv
import os

IN_PATH = os.path.join("data", "countypres_2000-2020.csv")
OUTPUT_DIR = "artifacts"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "election_report.csv")

def count_votes(path):

    with open(path, "r") as in_file:
        dict_reader = csv.DictReader(in_file)

        counts = {}

        for row in dict_reader:
            year = row['year']
            state = row['state_po']
            candidate = row['candidate']
        
            if year == '2020':
                try:
                    candidate_votes = int(row['candidatevotes'])
                    if (year, state, candidate) in counts:
                        counts[year, state, candidate] += candidate_votes
                    else:
                        counts[year, state, candidate] = candidate_votes
                except ValueError:
                    pass

    return counts

def get_rows(counts):
    
    rows = list()
    for k in counts:
        tt = list(k)
        ff = tt.append(counts[k])
        rows.append(tt)

    return rows

def sort_rows(list_):
    
    list_.sort(key=lambda x:x[3], reverse = True)
    list_.sort(key=lambda x:x[1])

    return list_

def write_rows(rows):

    with open(OUTPUT_PATH, 'w+') as out_file:
        csv_writer = csv.writer(out_file)

        header = ['year', 'state_code', 'candidate', 'votes']
        data = rows 

        csv_writer.writerow(header)
        csv_writer.writerows(data)

if __name__ == "__main__":

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    counts = count_votes(IN_PATH)
    rows = get_rows(counts)
    sorted_rows = sort_rows(rows)
    write_rows(sorted_rows)
