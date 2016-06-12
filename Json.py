class Json_Data():
#ACCEPTS A STRING
    def search_results_json(find_results):
        find_results = find_results.split(", \n")
        json_data = "results: ["

        for results in find_results:
            json_data += "{Item:" + results + "},"
        size = len(json_data) - 1
        json_data = json_data[:size] + json_data[size+1:]
        json_data += "]"
        return json_data
