import streamlit as st

def main():
    st.title("Network Service Enumeration Techniques Quiz")
    st.markdown("This quiz will test your understanding of common network service enumeration techniques, including LDAP, NTP, NFS, SMTP, and DNS. By the end of this quiz, you'll be able to identify various protocols used, tools for enumeration, and the types of information that can be gathered from these services.")

    questions = [
        {
            "question": "What is the primary purpose of LDAP?",
            "options": [
                "To synchronize clocks across network devices",
                "To transfer files over a network",
                "To manage email services",
                "To access and maintain directory information services"
            ],
            "answer": "To access and maintain directory information services",
            "explanation": "LDAP (Lightweight Directory Access Protocol) is used for accessing and maintaining distributed directory information services, like those in Active Directory."
        },
        {
            "question": "Which of the following protocols uses UDP Port 123 as its primary means of communication?",
            "options": [
                "LDAP",
                "NTP",
                "NFS",
                "SMTP"
            ],
            "answer": "NTP",
            "explanation": "Network Time Protocol (NTP) uses UDP Port 123 to synchronize the clocks of network devices."
        },
        {
            "question": "What type of information can an attacker gather by querying an NTP server?",
            "options": [
                "Email addresses and passwords",
                "List of hosts connected to the NTP server, client IP addresses, system names and operating systems",
                "Credit card details",
                "Social media profiles"
            ],
            "answer": "List of hosts connected to the NTP server, client IP addresses, system names and operating systems",
            "explanation": "Attackers can query an NTP server to gather valuable information such as a list of hosts, their IP addresses, system names and operating systems."
        },
          {
            "question": "What is the purpose of NFS (Network File System)?",
            "options": [
                "To synchronize time across network devices",
                "To provide email services",
                 "To allow hosts to mount file systems over a network",
                "To manage DNS records"
            ],
            "answer": "To allow hosts to mount file systems over a network",
            "explanation": "NFS allows hosts running different operating systems to mount file systems over a network, enabling access to shared files."
         },
        {
            "question": "Which of the following is NOT a command that is used for SMTP enumeration?",
            "options": [
                 "VRFY",
                "RCPT TO",
                 "EXPN",
                "SNMP"
            ],
            "answer": "SNMP",
            "explanation": "VRFY, RCPT TO, and EXPN are used for SMTP enumeration. SNMP (Simple Network Management Protocol) is for device management."
        },
        {
             "question": "What is one of the functions of the SMTP command `EXPN`?",
             "options": [
                "To identify the domain name of a sender",
                "To verify mailboxes on local hosts",
                "To specify message recipients",
                "To specify the maximum supported file size"
            ],
           "answer": "To verify mailboxes on local hosts",
            "explanation": "The SMTP command EXPN can be used to verify the existence of mailboxes on local hosts."
         },
         {
            "question": "What does DNS enumeration primarily focus on?",
             "options": [
                "Identifying user email addresses",
                "Detecting and listing DNS records associated with a domain",
                "Finding available file shares",
                "Scanning for open ports"
            ],
           "answer": "Detecting and listing DNS records associated with a domain",
           "explanation": "DNS enumeration detects and enumerates all possible DNS records from a domain, including hostnames, record types, and IP addresses."
        },
        {
            "question": "What is a DNS zone transfer?",
            "options": [
                "A method to send emails securely",
                 "A process where a DNS server passes a copy of the database records to another DNS server",
                "The process of transferring files using NFS",
                 "A way to connect to an NTP server"
            ],
             "answer": "A process where a DNS server passes a copy of the database records to another DNS server",
             "explanation": "A DNS zone transfer is when a DNS server passes a copy of its database records to another DNS server."
        },
          {
            "question": "Which two tools were used in the lab to perform DNS enumeration?",
            "options": [
                 "nmap and wireshark",
                "NSLookup and dig",
                "Telnet and NetScan Tool Pro",
                "ntpdc and ntptrace"
            ],
             "answer": "NSLookup and dig",
             "explanation": "The two tools used for DNS enumeration in the lab were NSLookup and dig."
        },
        {
             "question": "What is one measure that can be taken as a countermeasure for DNS enumeration?",
            "options": [
                 "Enabling zone transfers to untrusted hosts",
                "Ensuring that private hostnames are referenced in public DNS records",
                 "Disabling zone transfers to untrusted hosts",
                "Using free registration services for domains"
           ],
            "answer": "Disabling zone transfers to untrusted hosts",
            "explanation": "Disabling zone transfers by untrusted hosts can help prevent unauthorized DNS enumeration."
        }
    ]


    if 'score' not in st.session_state:
        st.session_state.score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}:")
        st.write(q["question"])
        selected_option = st.radio(f"Select an option:", q["options"], key=f"q{i}", index=None) # index=None to prevent default selection

        if st.button("Check Answer", key=f"btn{i}"):
            if selected_option == q["answer"]:
                st.session_state.score += 1
                st.success("Correct!")
            elif selected_option is not None:
                st.error(f"Incorrect. The correct answer is: {q['answer']}")
            
            if selected_option is not None:
              with st.expander("Explanation"):
                st.write(q["explanation"])
            st.write("---") # adds a line after each question

    st.header("Quiz Results")
    st.write(f"Your final score is: {st.session_state.score}/{len(questions)}")

if __name__ == "__main__":
    main()