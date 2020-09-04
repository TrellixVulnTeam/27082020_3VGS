import copy


def mkfile(name, meta={}):
    '''Return file node.'''
    return {
        'name': name,
        'meta': meta,
        'type': 'file',
    }


def mkdir(name, children=[], meta={}):
    '''Return directory node.'''
    return {
        'name': name,
        'children': children,
        'meta': meta,
        'type': 'directory',
    }


def is_directory(node):
    '''Check is node a directory.'''
    return node.get('type') == 'directory'


def is_file(node):
    '''Check is node a file.'''
    return node.get('type') == 'file'


def get_children(directory):
    '''Return children of node.'''
    return directory.get('children')


def get_meta(node):
    '''Return meta of node.'''
    return node.get('meta')


def get_name(node):
    '''Return name of node.'''
    return node.get('name')


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)

    walk(tree)
    return result


def compress_images(tree):
    dir = get_name(tree)
    print(dir)
    children = get_children(tree)
    print(children)
    b_dir = is_directory(tree)
    print(b_dir)
    file = filter(is_file(tree), tree)
    print(list(file))




tree = mkdir(
    'my documents',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)
compress_images(tree)

test_tree = {
    'name': 'my documents',
    'type': 'directory',
    'children': [
        {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
        {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
    ],
    'meta': {'hide': False},
}