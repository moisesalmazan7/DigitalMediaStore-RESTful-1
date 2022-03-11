from app.extensions.schema import ma
from app.models.tracks import Track


class TrackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Track

    id = ma.auto_field(dump_only=True)


class TrackArgsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Track
        include_fk = True

    id = ma.auto_field(dump_only=True)
