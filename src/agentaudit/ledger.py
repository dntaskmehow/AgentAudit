from datetime import datetime
from pydantic import BaseModel

class AuditEvent(BaseModel):
    timestamp: str = datetime.utcnow().isoformat()
    agent_id: str
    action: str
    tokens_used: int
    cost_usd: float
    status: str

class AuditLedger:
    def __init__(self, ledger_file: str = "audit_ledger.jsonl"):
        self.ledger_file = ledger_file
    def record(self, event: AuditEvent):
        with open(self.ledger_file, "a", encoding="utf-8") as f:
            f.write(event.model_dump_json() + "\n")
