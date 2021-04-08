def can_build(env, platform):
    return env["thread_support"]


def configure(env):
    pass


def get_doc_classes():
    return [
        "ThreadPool",
        "ThreadPoolJob",
        "ThreadPoolExecuteJob",
    ]


def get_doc_path():
    return "doc_classes"
