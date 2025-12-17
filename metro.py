import qrcode
from gtts import gTTS
import streamlit as st
from io import BytesIO
import uuid

# QR GENERATION FUNCTION
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


# STREAMLIT UI
st.set_page_config(page_title="Metro Ticket Booking", page_icon="🚆")
st.title("🚆 Metro Ticket Booking System")

stations = ["Ameerpet", "Miyapur", "LB Nagar", "KPHB", "JNTU"]
name = st.text_input("Passenger Name")
source = st.selectbox("Source Station", stations)
destination = st.selectbox("Destination Station", stations)
no_tickets = st.number_input("Number of Tickets", min_value=1, value=1)

price_per_ticket = 30
total_amount = no_tickets * price_per_ticket
st.info(f"Total Amount: ₹{total_amount}")

# BOOK TICKET
if st.button("Book Ticket"):

    if name.strip() == "":
        st.error("Please enter passenger name.")
    elif source == destination:
        st.error("Source and Destination cannot be same.")
    else:
        st.success("Tickets Booked Successfully 🎉")

        st.subheader("🎫 Ticket QRs")

        # Loop → one QR per ticket
        for i in range(1, no_tickets + 1):
            ticket_id = str(uuid.uuid4())[:8]

            qr_data = (
                f"Ticket ID: {ticket_id}\n"
                f"Passenger: {name}\n"
                 f"From: {source}\n"
                f"To: {destination}\n"
                f"Ticket No: {i}\n"
                f"Amount: ₹{price_per_ticket}"
            )

            qr_img = generate_qr(qr_data)

            buf = BytesIO()
            qr_img.save(buf, format="PNG")
            qr_bytes = buf.getvalue()

            st.markdown(f"### Ticket {i}")
            st.image(qr_bytes, width=220)
