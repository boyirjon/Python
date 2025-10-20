# Customer Purchases Analysis:

import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

customers_df = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM customers", conn)
invoices_df = pd.read_sql_query("SELECT CustomerId, Total FROM invoices", conn)

customer_total = invoices_df.groupby("CustomerId")["Total"].sum().reset_index()
customer_total.rename(columns={"Total": "TotalSpent"}, inplace=True)

merged_df = pd.merge(customers_df, customer_total, on="CustomerId")

top5_customers = merged_df.sort_values(by="TotalSpent", ascending=False).head(5)

result = top5_customers[["CustomerId", "FirstName", "LastName", "TotalSpent"]]

print("Top 5 Customers by Total Purchase Amount:\n")
print(result)

conn.close()

# Album vs. Individual Track Purchases:

import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM invoices", conn)
invoice_items = pd.read_sql_query("SELECT InvoiceId, TrackId FROM invoice_items", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM tracks", conn)
albums = pd.read_sql_query("SELECT AlbumId, Title FROM albums", conn)

merged = invoice_items.merge(tracks, on="TrackId").merge(invoices, on="InvoiceId")

album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracks"}, inplace=True)

customer_album_tracks = (
    merged.groupby(["CustomerId", "AlbumId"])["TrackId"]
    .nunique()
    .reset_index()
)
customer_album_tracks.rename(columns={"TrackId": "PurchasedTracks"}, inplace=True)

customer_album_tracks = customer_album_tracks.merge(album_track_counts, on="AlbumId")

customer_album_tracks["FullAlbumBought"] = customer_album_tracks["PurchasedTracks"] == customer_album_tracks["TotalTracks"]

customer_pref = (
    customer_album_tracks.groupby("CustomerId")["FullAlbumBought"]
    .any()
    .reset_index()
)
customer_pref["Preference"] = customer_pref["FullAlbumBought"].apply(
    lambda x: "Full Albums" if x else "Individual Tracks"
)

summary = (
    customer_pref["Preference"]
    .value_counts(normalize=True)
    .reset_index()
    .rename(columns={"index": "Purchase Type", "Preference": "Percentage"})
)

summary["Percentage"] = (summary["Percentage"] * 100).round(2)

print("Customer Purchase Preference Summary:\n")
print(summary)

conn.close()
