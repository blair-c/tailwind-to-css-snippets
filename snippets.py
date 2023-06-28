import json

snippets = {
    'min-': {
        'prefix': 'min-',
        'body': ['@media (min-width: $1) {', '\t$0', '}']
    },
    'sm': {
        'prefix': 'sm',
        'body': ['@media (min-width: 640px) {', '\t$1', '}']
    },
    'md': {
        'prefix': 'md',
        'body': ['@media (min-width: 768px) {', '\t$1', '}']
    },
    'lg': {
        'prefix': 'lg',
        'body': ['@media (min-width: 1024px) {', '\t$1', '}']
    },
    'xl': {
        'prefix': 'xl',
        'body': ['@media (min-width: 1280px) {', '\t$1', '}']
    },
    '2xl': {
        'prefix': '2xl',
        'body': ['@media (min-width: 1536px) {', '\t$1', '}']
    },
    'max-': {
        'prefix': 'max-',
        'body': ['@media (max-width: $1) {', '\t$0', '}']
    },
    'max-sm': {
        'prefix': 'max-sm',
        'body': ['@media not all and (min-width: 640px) {', '\t$1', '}']
    },
    'max-md': {
        'prefix': 'max-md',
        'body': ['@media not all and (min-width: 768px) {', '\t$1', '}']
    },
    'max-lg': {
        'prefix': 'max-lg',
        'body': ['@media not all and (min-width: 1024px) {', '\t$1', '}']
    },
    'max-xl': {
        'prefix': 'max-xl',
        'body': ['@media not all and (min-width: 1280px) {', '\t$1', '}']
    },
    'max-2xl': {
        'prefix': 'max-2xl',
        'body': ['@media not all and (min-width: 1536px) {', '\t$1', '}']
    },
    'dark': {
        'prefix': 'dark',
        'body': ['@media (prefers-color-scheme: dark) {', '\t$1', '}']
    },
    'portrait': {
        'prefix': 'portrait',
        'body': ['@media (orientation: portrait) {', '\t$1', '}']
    },
    'landscape': {
        'prefix': 'landscape',
        'body': ['@media (orientation: landscape) {', '\t$1', '}']
    },
    'motion-safe': {
        'prefix': 'motion-safe',
        'body': ['@media (prefers-reduced-motion: no-preference) {', '\t$1', '}']
    },
    'motion-reduce': {
        'prefix': 'motion-reduce',
        'body': ['@media (prefers-reduced-motion: reduce) {', '\t$1', '}']
    },
    'contrast-more': {
        'prefix': 'contrast-more',
        'body': ['@media (prefers-contrast: more) {', '\t$1', '}']
    },
    'contrast-less': {
        'prefix': 'contrast-less',
        'body': ['@media (prefers-contrast: less) {', '\t$1', '}']
    },
    'print': {
        'prefix': 'print',
        'body': ['@media print {', '\t$1', '}']
    },
    'supports-': {
        'prefix': 'supports-',
        'body': ['@supports ($1) {', '\t$0', '}']
    }
}

with open('scrape/scrape.json', 'r') as f:
    scrape = json.load(f)

for d in scrape:
    [[prefix, body]] = d.items()
    snippets[prefix] = {
        'prefix': prefix,
        'body': body
    }

if __name__ == '__main__':
    with open('snippets/css.json', 'w') as f:
        json.dump(snippets, f, indent=2)
