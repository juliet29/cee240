import pandas as pd

TEMPLATE_PATH = "../../../Documents/ClassDocs/cee240Docs/Cost Schedules/PayAppTemplate.xlsx"

dft = pd.read_excel(TEMPLATE_PATH , sheet_name=2, engine="openpyxl", skiprows=range(13), usecols="B")

# initialize dict with the categories
categories = list(dft.iloc[0:33,0])
empty = [i for i in range(len(categories))]
cd = { k:v for (k,v) in zip(categories, empty)} # cd = category dict

cd["BP 1A Structural Concrete"] = ["erect concrete deck","pour concrete"]
cd["BP 1B Exterior Glass & GFRC"] = ["curtain wall"]
cd["BP 1C Shoring"] = ["shoring"]
cd["BP 1D HVAC & Plumbing"] = ["MEP", "verify", "storm drain", "pipes"]
cd["BP 1E Electrical"] = ["MEP", "light"]
cd["BP 1F Elevators"] = ["elevator"]
cd["BP 2A Drywall & Metal Framing"] = ["install flooring", "install cieling", "install interior partitions" ]
cd["BP 2B Fire Protection"] = ["fire"]
cd["BP 2C Structural Steel"] = ["steel topping", "columns", "rebar"]
cd["BP 3A Drilled Piers"] = ["piles"]
cd["BP 3B Reinforcing Steel"] = ["seismic"]
cd["BP 3C Grading & Paving"] = ["paving", "subgrade"]
cd["BP 3D Demo"] = ["demo", "remove"]
cd["BP 4A Metal Decking"] = ["erect steel deck"]
cd["BP 4B Roofing & Waterproofing"] = ["roof"]
# cd["BP 4D Flashing & Sheetmetal"] = [] skip empty
cd["BP 4H Doors, Frames, Hardware"] = ["door", "doors"]
cd["BP 4J Coiling Doors"] = ["coiling"]
cd["BP 5C Test & Balance"] = ["testing"]
cd["BP 5D Painting"] = ["paint"]
cd["BP 5E Resilient Flooring"] = ["floor finishes"]
cd["BP 5F Misc Specialties"] = ["plaster"]
cd["BP 6A Landscaping"] = ["Courtyard"]
cd["BP 6B Wall Protection"] = ["patching"]