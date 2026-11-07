import logging
import uuid
import os
import datetime
import inngest
import inngest.fast_api

from dotenv import load_dotenv
from fastapi import FastAPI
from inngest.experimental import ai

load_dotenv()

inngest_client = inngest.Inngest(
    app_id="rag_app",
    logger=logging.getLogger("uvicorn"),
    is_production=False,
    serializer=inngest.PydanticSerializer()
)

@inngest_client.create_function(
    fn_id="RAG: Ingest PDF",
    trigger=inngest.TriggerEvent(event="rag/ingest_pdf")
)
async def rag_ingest_pdf(ctx: inngest.Context):
    return {"message": "PDF ingested successfully"}

app = FastAPI()

inngest.fast_api.serve(app, inngest_client, [rag_ingest_pdf])