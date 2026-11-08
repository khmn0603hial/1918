"""Bundle the tracked development HTML and local media into one offline HTML."""
from pathlib import Path
import argparse,base64,hashlib,json

ROOT=Path(__file__).resolve().parent.parent

def bundle():
    text=(ROOT/'index.html').read_text(encoding='utf-8')
    manifest=json.loads((ROOT/'assets/manifest.json').read_text(encoding='utf-8'))
    for relative,entry in manifest['assets'].items():
        data=(ROOT/relative).read_bytes()
        if hashlib.sha256(data).hexdigest()!=entry['sha256']:
            raise ValueError('Asset checksum mismatch: '+relative)
        text=text.replace(relative,'data:'+entry['mime']+';base64,'+base64.b64encode(data).decode('ascii'))
    if manifest['baseline'].get('newline')=='CRLF':
        text=text.replace('\n','\r\n')
    return text.encode('utf-8')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--verify-baseline',action='store_true',help='Require a byte-identical V17.7 baseline bundle.')
    args=parser.parse_args()
    data=bundle();digest=hashlib.sha256(data).hexdigest()
    if args.verify_baseline:
        manifest=json.loads((ROOT/'assets/manifest.json').read_text(encoding='utf-8'))
        if digest!=manifest['baseline']['sha256']:raise SystemExit('Baseline SHA-256 mismatch')
        print('V17.7 baseline verified byte for byte: '+digest)
    if args.output or not args.verify_baseline:
        target=args.output or ROOT/'dist'/('1918_V'+(ROOT/'VERSION').read_text().strip()+'.html')
        target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        print(str(target))
