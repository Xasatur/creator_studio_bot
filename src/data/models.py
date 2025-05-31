# src/data/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
import datetime
from src.data.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    discord_id = Column(String, unique=True)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # User profile data
    bio = Column(Text, nullable=True)
    commission_status = Column(String, default="closed")

    # Relationships
    portfolios = relationship("Portfolio", back_populates="user")

class Portfolio(Base):
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="portfolios")
    items = relationship("PortfolioItem", back_populates="portfolio")

class PortfolioItem(Base):
    __tablename__ = 'portfolio_items'

    id = Column(Integer, primary_key=True)
    portfolio_id = Column(Integer, ForeignKey('portfolios.id'))
    title = Column(String)
    description = Column(Text, nullable=True)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    portfolio = relationship("Portfolio", back_populates="items")
