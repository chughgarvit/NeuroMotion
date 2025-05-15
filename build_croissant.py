# build_croissant.py
import json
import mlcroissant as mlc

# 1. Top‐level metadata
md = mlc.Metadata(
    name="movesense",
    description="description of movesense.",
    license="https://creativecommons.org/licenses/by/4.0/",
    keywords=["imu", "hrv", "combined"],
    version="1.0.0",
    creators=[                              # note plural
        mlc.Person(name="Garvit Chugh", email="chugh.2@iitj.ac.in")
    ]
)

# 2. Distributions: use camelCase here!
md.distribution = [
    mlc.FileObject(
        id="movesense-repo",
        name="movesense GitHub repository",
        description="GitHub repo archive for the movesense dataset",
        contentUrl="https://github.com/chughgarvit/movesense/archive/refs/heads/main.zip",
        encodingFormat="application/zip",
    )
]

# 3. Record-set(s) and schema (unchanged)
default_rs = mlc.RecordSet(
    id="default",
    name="Default split",
    fields=[
        mlc.Field(
            id="imu",
            name="imu",
            description="IMU CSV folder",
            dataType=mlc.DataType.URL,
            source=mlc.Source(fileObject="movesense-repo")
        ),
        mlc.Field(
            id="hrv",
            name="hrv",
            description="HRV JSON folder",
            dataType=mlc.DataType.URL,
            source=mlc.Source(fileObject="movesense-repo")
        )
    ]
)
md.recordSets = [default_rs]               # camelCase here too

# 4. Write out the JSON-LD
with open("metadata.json", "w") as f:
    json.dump(md.to_json(), f, indent=2)

print("Generated metadata.json successfully.")
