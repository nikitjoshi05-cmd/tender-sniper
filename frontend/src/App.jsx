import React, { useState } from 'react';
import { Target, Search, Activity, FileCheck, XCircle, CheckCircle2, Loader2, Server } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

function App() {
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const startSniper = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://127.0.0.1:8000/agent/full-run');
      if (!response.ok) throw new Error('Network response was not ok');
      const result = await response.json();
      if (result.error) throw new Error(result.error);
      setData(result);
    } catch (err) {
      setError(err.message || 'Failed to connect to the Sniper Engine.');
    } finally {
      setLoading(false);
    }
  };

  const totals = data?.results ? data.results.length : 0;
  const applied = data?.results ? data.results.filter(r => r.application?.status === 'applied').length : 0;
  const skipped = totals - applied;

  return (
    <div className="container">
      <header>
        <div className="logo">
          <Target className="logo-icon" size={32} />
          <span>Tender Sniper</span>
        </div>
        <button 
          className="btn btn-primary" 
          onClick={startSniper} 
          disabled={loading}
        >
          {loading ? (
            <><Loader2 size={18} className="spinner" /> Analyzing Protocol...</>
          ) : (
            <><Activity size={18} /> Start Auto-Sniper</>
          )}
        </button>
      </header>

      <AnimatePresence>
        {error && (
          <motion.div 
            initial={{ opacity: 0, y: -10 }} 
            animate={{ opacity: 1, y: 0 }} 
            exit={{ opacity: 0 }}
            style={{ background: 'rgba(255, 51, 102, 0.1)', color: 'var(--danger-color)', padding: '1rem', borderRadius: '8px', marginBottom: '2rem', border: '1px solid rgba(255, 51, 102, 0.3)' }}
          >
            <Server size={18} style={{ display: 'inline', marginRight: '0.5rem', verticalAlign: 'middle' }} />
            Connection Error: {error}
          </motion.div>
        )}
      </AnimatePresence>

      {!data && !loading && !error && (
        <div className="empty-state">
          <Search size={48} className="empty-icon" />
          <h3>System Idle</h3>
          <p style={{ marginTop: '0.5rem' }}>Click "Start Auto-Sniper" to initialize the autonomous tender scraping and application pipeline.</p>
        </div>
      )}

      {loading && (
        <div className="loader-wrapper">
          <Loader2 size={48} className="spinner" />
          <h3>Neural Network Processing...</h3>
          <p style={{color: 'var(--text-secondary)'}}>Scraping, parsing, matching, and applying autonomously.</p>
        </div>
      )}
      
      {data && !loading && (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.5 }}>
          <div className="metrics">
            <div className="metric-card">
              <span className="metric-label">Tenders Scanned</span>
              <span className="metric-value">{totals}</span>
            </div>
            <div className="metric-card">
              <span className="metric-label">Applications Submitted</span>
              <span className="metric-value" style={{ background: 'linear-gradient(to right, #00ff88, #00bfff)', WebkitBackgroundClip: 'text'}}>{applied}</span>
            </div>
            <div className="metric-card">
              <span className="metric-label">Tenders Skipped</span>
              <span className="metric-value">{skipped}</span>
            </div>
          </div>

          <div className="tender-grid">
            {data.results.map((item, idx) => {
              const isMatch = item.match.is_match;
              return (
                <motion.div 
                  key={idx}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: idx * 0.1 }}
                  className={`tender-card ${isMatch ? 'tender-match' : 'tender-skip'}`}
                >
                  <div className="tender-header">
                    <div>
                      <h3 className="tender-title">{item.tender.title}</h3>
                      <div className="tender-meta">
                        <span>Budget: {item.tender.budget}</span>
                        <span>Deadline: {item.tender.deadline}</span>
                      </div>
                    </div>
                    <div className={`badge ${isMatch ? 'badge-applied' : 'badge-skipped'}`}>
                      {isMatch ? (
                        <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                          <FileCheck size={14} /> APPLIED
                        </span>
                      ) : (
                        <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                          <XCircle size={14} /> SKIPPED
                        </span>
                      )}
                    </div>
                  </div>
                  
                  <div className="reasoning-box">
                    <strong>AI Evaluation:</strong>
                    <p style={{ marginTop: '0.5rem', whiteSpace: 'pre-wrap' }}>{item.reasoning}</p>
                  </div>
                </motion.div>
              );
            })}
          </div>
        </motion.div>
      )}
    </div>
  );
}

export default App;
