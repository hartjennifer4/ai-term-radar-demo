import json
import re
from collections import Counter

TEXT = '''
New AI models and repos spotted today: DeepSeek-Harness, AgentSkills, OpenIntelligentUI.
The new model deepseek-harness is trending on GitHub and Hugging Face.
Claude Skills and MCP servers are appearing in Ai startup workflows.
A tiny OCR model called Indra runs on CPU and beats tesseract.
OpenUI powers generative-ui chat interfaces with streaming UI.
'''
KNOWN = {'AI', 'LLM', 'GPT', 'OpenAI', 'GitHub', 'Hugging', 'Face', 'MCP', 'CPU', 'OCR', 'Agent', 'Agents', 'API', 'UI', 'React', 'Claude', 'Skills', 'OpenUI'}
CONTEXT = {'model', 'models', 'agent', 'agents', 'ocr', 'llm', 'repo', 'repos', 'tool', 'server', 'servers', 'skill', 'skills', 'ui', 'chat', 'workflow', 'workflows'}
STOP = {'New', 'The', 'A', 'An', 'And', 'For', 'With', 'From', 'Today', 'Tiny', 'Runs', 'Beats', 'Powers', 'Called', 'Spotted', 'Trending', 'Appearing', 'Startup'}

def score_terms(text):
    words = re.findall(r'[A-Za-z][A-Za-z0-9-]+', text)
    scores = Counter()
    for word in words:
        if word in STOP or word in KNOWN:
            continue
        s = 1
        if '-' in word or word.lower() != word or any(ch.isdigit() for ch in word):
            s += 1
        lower = text.lower()
        if any(ctx in lower for ctx in CONTEXT):
            s += 1
        scores[word] += s
    return scores

def main():
    scores = score_terms(TEXT)
    top = scores.most_common(10)
    print('New AI term radar candidates:')
    for term, score in top:
        print(f'- {term} (score={score})')
    print('JSON:', json.dumps([{'term': t, 'score': s} for t, s in top], ensure_ascii=False))

if __name__ == '__main__':
    main()