# Databricks notebook source
dbutils.widgets.text("bronze_schema", "", "bronze_schema")
bronze_schema = dbutils.widgets.get("bronze_schema")
print(bronze_schema)
