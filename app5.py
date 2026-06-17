# 5. CORE WORKSPACE SURFACE INTERFACES
st.markdown('<div class="active-workspace-surface">', unsafe_allow_html=True)

st.markdown('<div class="app-brand-tag">Kanpur Division Module</div>', unsafe_allow_html=True)
st.markdown('<div class="app-main-title">Pitch Pro</div>', unsafe_allow_html=True)

# THE LANDING TELEMETRY PANEL: Disappears automatically when a workspace module is selected.
if not st.session_state.selected_module:
    st.markdown("""
        <div class="telemetry-card">
            <div class="app-brand-tag" style="font-size:10px; margin-bottom:12px; color:rgba(255,255,255,0.4);">Territory Market Share Snapshot</div>
            <div class="telemetry-grid">
                <div class="telemetry-item">
                    <div class="telemetry-val leader-color">38.6%</div>
                    <div class="telemetry-lbl">🟢 PhonePe</div>
                </div>
                <div class="telemetry-item">
                    <div class="telemetry-val">37.6%</div>
                    <div class="telemetry-lbl">Paytm</div>
                </div>
                <div class="telemetry-item">
                    <div class="telemetry-val">9.6%</div>
                    <div class="telemetry-lbl">BharatPe</div>
                </div>
                <div class="telemetry-item">
                    <div class="telemetry-val">5.8%</div>
                    <div class="telemetry-lbl">Google Pay</div>
                </div>
                <div class="telemetry-item">
                    <div class="telemetry-val">8.4%</div>
                    <div class="telemetry-lbl">Others</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Symmetrical Card Grid Generation Systems (Clean line breaks, original short names)
row1_cols = st.columns(2)
# ... (rest of your existing code remains unchanged)
