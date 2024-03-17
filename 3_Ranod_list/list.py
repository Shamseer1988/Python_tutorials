list_state_india = ["Andhra Pradesh.", "Arunachal Pradesh.", "Assam. Bihar.", "Chhattisgarh.", "Goa.", "Gujarat.",
                    "Haryana.", "Himachal Pradesh.", "Jammu and Kashmir.", "Jharkhand.", "Karnataka."]

fruites = ["Apple", "Orrange" , "Banana"]

list_state_india[1] = "Shamseer"

list_state_india.append("makkanamchery")
list_state_india.extend(["ext_a", "extend_b"])

print(list_state_india[13])

number_item = len(list_state_india)

print(number_item)

# Merge two lists
merged_list = [list_state_india, fruites]

print(merged_list)
