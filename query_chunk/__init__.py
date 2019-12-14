def chunk_page(source_qs, chunk_size, query_log=None):
    field = source_qs.model._meta.pk
    order_by_field = field.attname

    source_qs = source_qs.order_by(order_by_field)
    queryset = source_qs

    page = 1

    while True:
        position = page * chunk_size
        items = queryset[position - chunk_size:position]

        if query_log is not None:
            query_log.write('{items.query}\n'.format(items=items))
        items = list(items)
        nb_items = len(items)

        if nb_items == 0:
            return

        page += 1
        yield items

        if nb_items < chunk_size:
            return


def chunk(source_qs, chunk_size, query_log=None):
    for page in chunk_page(source_qs, chunk_size, query_log=query_log):
        for item in page:
            yield item
