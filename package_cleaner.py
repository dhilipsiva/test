import csv

exclude_set = {"com", "org"}
f = open('Test.csv', 'r')
csv_reader = csv.reader(f)
detected_packages = []
for row in csv_reader:
    packages = row[0]
    package_list = packages.split(",")
    detected_packages_app = []
    for package in package_list:
        sdk = set(package.split("."))
        cleaned_package = list(sdk - exclude_set)
        if len(cleaned_package) > 0:
            detected_packages_app.append(cleaned_package[0])
    detected_packages.append(list(set(detected_packages_app)))

print(detected_packages)
