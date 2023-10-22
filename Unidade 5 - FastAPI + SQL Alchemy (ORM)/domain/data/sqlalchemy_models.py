import datetime
from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Signup(Base):
    __tablename__ = "signup"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str]
    password: Mapped[str]


class Login(Base):
    __tablename__ = "login"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str]
    password: Mapped[str]
    date_approved = Mapped[Date]
    user_type = Mapped[int]

    trainers: Mapped['Profile_Trainers'] = relationship(back_populates="login", uselist=False)
    members: Mapped['Profile_Members'] = relationship(back_populates="login", uselist=False)


class Profile_Trainers(Base):
    __tablename__ = "profile_trainers"

    id: Mapped[int] = mapped_column(ForeignKey('login.id'), primary_key=True, index=True)
    firstname: Mapped[str]
    lastname: Mapped[str]
    age: Mapped[int]
    position: Mapped[str]
    tenure: Mapped[float]
    shift: Mapped[int]

    login: Mapped['Login'] = relationship(back_populates="trainers")
    gclass: Mapped['Gym_Class'] = relationship(back_populates="trainers")


class Profile_Members(Base):
    __tablename__ = "profile_members"

    id: Mapped[int] = mapped_column(ForeignKey('login.id'), primary_key=True, index=True)
    firstname: Mapped[str]
    lastname: Mapped[str]
    age: Mapped[int]
    height: Mapped[float]
    weight: Mapped[float]
    membership_type: Mapped[str]
    trainer_id: Mapped[int] = mapped_column(ForeignKey('profile_trainers.id'))

    login: Mapped['Login'] = relationship(back_populates="members")
    attendance: Mapped['Attendance_Member'] = relationship(back_populates="members")
    gclass: Mapped['Gym_Class'] = relationship(back_populates="members")


class Attendance_Member(Base):
    __tablename__ = "attendance_member"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    member_id: Mapped[int] = mapped_column(ForeignKey('profile_members.id'))
    timeout: Mapped[datetime.time]
    timein: Mapped[datetime.time]
    date_log: Mapped[datetime.date]

    members: Mapped['Profile_Members'] = relationship(back_populates="attendance")


class Gym_Class(Base):
    __tablename__ = "gym_class"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    member_id: Mapped[int] = mapped_column(ForeignKey('profile_members.id'))
    trainer_id: Mapped[int] = mapped_column(ForeignKey('profile_trainers.id'))
    approved_id: Mapped[int]

    trainers: Mapped['Profile_Trainers'] = relationship(back_populates="gclass")
    members: Mapped['Profile_Members'] = relationship(back_populates="gclass")
