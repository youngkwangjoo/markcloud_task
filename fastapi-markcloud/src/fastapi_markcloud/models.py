from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Trademark(Base):
    __tablename__ = "trademarks"

    id = Column(Integer, primary_key=True, index=True)
    productName = Column(String(255), nullable=False)
    productNameEng = Column(String(255), nullable=True)

    applicationNumber = Column(String(50), nullable=False)
    applicationDate = Column(String(8), nullable=True)

    registerStatus = Column(String(50), nullable=True)

    publicationNumber = Column(String(50), nullable=True)
    publicationDate = Column(String(8), nullable=True)

    registrationNumber = Column(String(50), nullable=True)
    registrationDate = Column(String(8), nullable=True)

    internationalRegNumbers = Column(JSON, nullable=True)
    internationalRegDate = Column(String(8), nullable=True)

    priorityClaimNumList = Column(JSON, nullable=True)
    priorityClaimDateList = Column(JSON, nullable=True)

    asignProductMainCodeList = Column(JSON, nullable=True)
    asignProductSubCodeList = Column(JSON, nullable=True)
    viennaCodeList = Column(JSON, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Trademark {self.productName}>"
