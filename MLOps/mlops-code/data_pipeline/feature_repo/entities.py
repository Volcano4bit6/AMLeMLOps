from feast import Entity

account = Entity(
    name="Account",
    join_keys=["Account"],
    description="User id",
    tags={},
    owner="sontvh2002@gmail.com",
)
