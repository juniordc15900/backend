from sqlalchemy.orm import Session
from fastapi import HTTPException, status


from models import Filme


class FilmeRepository:

# métodos do CRUD

    # retorna todos os filmes
    @staticmethod
    def findAll(db: Session) -> list[Filme]:
        return db.query(Filme).all()

    # cria um novo filme
    @staticmethod
    def create(db: Session, filme: Filme) -> Filme:
        if filme.id:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Filme já existe"
        )
        else:
            db.add(filme)
        db.commit()
        return filme

    # retorna um filme pelo id
    @staticmethod
    def findById(db: Session, id: int) -> Filme:
        return db.query(Filme).filter(Filme.id == id).first()

    @staticmethod
    def exists(db: Session, id: int) -> bool:
        return db.query(Filme).filter(Filme.id == id).first() is not None

    # deleta um filme pelo id
    @staticmethod
    def delete(db: Session, id: int) -> None:
        filme = db.query(Filme).filter(Filme.id == id).first()
        if filme is not None:
            db.delete(filme)
            db.commit()