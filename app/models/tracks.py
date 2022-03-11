from app.extensions.database import BaseModelMixin, db

# from app.models import Album  # noqa:F401


class Track(db.Model, BaseModelMixin):
    __tablename__ = "Track"
    id = db.Column(name="TrackId", type_=db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(name="Name", type_=db.Unicode(200), nullable=False)
    # media_type_id = db.Column(name="MediaTypeId", type=db.Integer, nullalbe=False, default=1)
    composer = db.Column(name="Composer", type_=db.Unicode(220))
    miliseconds = db.Column(name="Miliseconds", type_=db.Integer, nullalbe=False)
    bytes = db.Column(name="Bytes", type_=db.Integer, default=None)
    unitprice = db.Column(name="UnitPrice", type_=db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f"<Tracks {self.name}>"

    def __str__(self):
        return self.name

    #     # def save(self):
    #     #     BaseModelMixin.save(self)
    #     #     self.id

    @classmethod
    def find_track_by_name(cls, name):
        return cls.simple_filter(name=name).first()
