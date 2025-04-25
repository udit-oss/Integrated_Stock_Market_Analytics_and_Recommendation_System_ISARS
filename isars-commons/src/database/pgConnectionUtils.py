import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from isars_commons.src.audit.loggerUtils import get_logger

logger = get_logger()

load_dotenv()


def get_database_url() -> str:
    """
    Build the SQLAlchemy database URL from environment variables:
      POSTGRES_USER, POSTGRES_PASSWORD,
      POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB
    """
    user = os.getenv("POSTGRES_USER", "isars_user")
    password = os.getenv("POSTGRES_PASSWORD", "securepassword")
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = os.getenv("POSTGRES_PORT", "5432")
    db_name = os.getenv("POSTGRES_DB", "isars_db")

    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
    logger.debug(f"Constructed database URL: {url}")
    return url


try:
    engine = create_engine(get_database_url(), echo=True)
    logger.info("SQLAlchemy engine created successfully.")
except Exception as e:
    logger.error(f"Failed to create SQLAlchemy engine: {e}")
    raise

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    """
    Dependency for providing a database session.
    Yields a SQLAlchemy Session instance and ensures closure.
    """
    db = SessionLocal()
    logger.debug("Database session opened.")
    try:
        yield db
    except Exception as e:
        logger.error(f"Error during DB session: {e}")
        raise
    finally:
        db.close()
        logger.debug("Database session closed.")
