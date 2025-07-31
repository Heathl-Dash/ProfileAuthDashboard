from .base import MaterializedView


class WeigthHistoryMonthly(MaterializedView):
    view_name="mv_weigth_history_monthly_mv"
    sql="""
        CREATE MATERIALIZED VIEW IF NOT EXISTS mv_peso_mensal AS
        SELECT *
        FROM "profileCore_weigthhistory"
        WHERE DATE_TRUNC('month', created_at) = DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month');
    """
    frequency="monthly"